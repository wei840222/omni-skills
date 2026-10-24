# Official Sources & Framework References

This document records the primary official documentation and framework references for modern Laravel development.

## Official Framework Documentation

- **Laravel Documentation (11.x Releases)**: [https://laravel.com/framework/docs/11.x/releases](https://laravel.com/framework/docs/11.x/releases)
  - Streamlined application structure, PHP 8.2+ requirements, default SQLite database, and per-second rate limiting.
- **Eloquent ORM & Relationship Optimization**: [https://laravel.com/framework/docs/11.x/eloquent](https://laravel.com/framework/docs/11.x/eloquent)
  - Eager loading (`with`), N+1 query prevention (`preventLazyLoading`), mass assignment protection (`$fillable`), and query caching.
- **Queues & Worker Lifecycle**: [https://laravel.com/framework/docs/11.x/queues](https://laravel.com/framework/docs/11.x/queues)
  - Database and Redis queue drivers, worker connection management, retry attempts, timeout handling, and failed jobs processing (`queue:failed`, `queue:retry`).
- **Artisan CLI & Task Scheduling**: [https://laravel.com/framework/docs/11.x/artisan](https://laravel.com/framework/docs/11.x/artisan)
  - Console command generation, route/config caching considerations, and schedule runners.
