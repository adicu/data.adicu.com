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

  Firewall <| |>
}
