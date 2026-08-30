# Rails Technical Guidelines

## Current Best Practices

- **Asset Pipeline:** Hotwire (Turbo/Stimulus) is the default for Rails 7+, eliminating the need for complex Webpack configurations for most setups. Import maps are preferred for vanilla JS.
- **Background Jobs:** ActiveJob with Sidekiq or Solid Queue. Solid Queue (database-backed queueing) is standard in Rails 8.
- **Database:** ActiveRecord now includes strict loading (`strict_loading!`) to proactively prevent N+1 queries by raising errors if relationships are not preloaded.
- **Authentication:** `has_secure_password` remains the standard for simple setups. Devise is widely used, and Rails 8 includes a built-in authentication generator.
- **Action Mailbox & Action Text:** Standard for handling inbound emails and rich text content.

## Verifiable Sources

- Rails Guides — Active Record Query Interface: https://guides.rubyonrails.org/active_record_querying.html
- Rails Guides — Active Record Associations: https://guides.rubyonrails.org/association_basics.html
- Rails Guides — Action Controller Overview: https://guides.rubyonrails.org/action_controller_overview.html
- Rails Guides — Rails Routing: https://guides.rubyonrails.org/routing.html
- Rails Guides — Active Job Basics: https://guides.rubyonrails.org/active_job_basics.html
- Rails Guides — Securing Rails Applications: https://guides.rubyonrails.org/security.html
- Rails Guides — Autoloading and Reloading Constants (Zeitwerk): https://guides.rubyonrails.org/autoloading_and_reloading_constants.html
- Hotwire / Turbo handbook: https://turbo.hotwired.dev/handbook/introduction
- Solid Queue README: https://github.com/rails/solid_queue
