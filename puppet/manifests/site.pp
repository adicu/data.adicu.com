node 'development.adicu.com' {
  exec { "apt-update":
      command => "/usr/bin/apt-get update"
  }

  Exec["apt-update"] -> Package <| |>

  include postgresql::server

  postgresql::db { 'data':
    user => 'adicu',
    password => 'development'
  }

  exec { "load_dev_data":
    command => '/usr/bin/sudo -u postgres psql data < /vagrant/development_dump.sql',
    require => Postgresql::Db['data']
  }

  include mongodb

  user { 'data':
    ensure => present,
    gid => 'users',
    home => '/home/data/',
    shell => '/bin/bash',
    managehome => true
  }

  class { 'python':
    virtualenv => true,
    dev => true
  }

  package { 'libcurl4-nss-dev':
    ensure => present
  }

  package { 'libxslt-dev':
    ensure => present
  }

  package { 'postgresql-server-dev-9.1':
    ensure => present
  }

  python::virtualenv { '/home/data/venv':
    ensure => present,
    version => '2.7',
    requirements => '/vagrant/requirements.txt',
    owner => 'data',
    group => 'users',
    require => [
      User['data'],
      Package['libcurl4-nss-dev'],
      Package['libxslt-dev'],
      Package['postgresql-server-dev-9.1'],
    ]
  }

  include supervisord

  supervisord::program { 'data_server':
    command         => "/bin/bash /vagrant/start_server.sh example",
    directory       => "/vagrant",
    user            => "data",
    stdout_logfile  => "/var/log/supervisor/data_server.log",
    redirect_stderr => true
  }

  exec { "restart_supervisor":
    command => "/usr/bin/sudo /etc/init.d/supervisor stop;
        /bin/sleep 1 && /usr/bin/sudo /etc/init.d/supervisor start",
    require => Supervisord::Program['data_server']
  }

  class { 'nginx': }

  nginx::resource::vhost { 'data.adicu.com':
    ensure => 'present',
    proxy  => 'http://localhost:3000'
  }

  Firewall <| |>
}
