node 'development.adicu.com' {
  include postgresql::server

  postgresql::db { 'data':
    user => 'adicu',
    password => 'development'
  }

  class { 'redis':
    redis_password => 'development'
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
    virtualenv => true
  }

  package { 'postgresql-server-dev-9.1':
    ensure => present
  }

  package { 'libcurl3':
    ensure => present
  }

  package { 'libxslt-dev':
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
      Package['postgresql-server-dev-9.1'],
      Package['libcurl3'],
      Package['libxslt-dev']
    ]
  }

  Firewall <| |>
}
