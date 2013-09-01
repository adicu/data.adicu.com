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

  Firewall <| |>
}
