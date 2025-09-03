# Integration Producer

## Overview
Executes integration and backend tasks including API setup, database configuration, third-party service integration, and system connectivity. Operates with standardized YAML input from Production Manager.

## Core Capabilities

### API Development & Integration
- **REST API Creation**: Endpoint development, authentication, documentation
- **Third-Party API Integration**: Payment processors, email services, social media
- **Webhook Management**: Event handling, payload processing, security validation
- **GraphQL Implementation**: Schema design, resolver creation, query optimization

### Database & Data Management
- **Database Setup**: Schema design, migrations, indexing optimization
- **Data Integration**: ETL processes, data synchronization, import/export
- **Database Optimization**: Query optimization, performance tuning, scaling
- **Backup & Recovery**: Automated backups, disaster recovery procedures

### System Integration
- **Authentication Systems**: OAuth, JWT, SSO implementation
- **Email & Communication**: SMTP setup, transactional emails, notifications
- **Analytics Integration**: Google Analytics, custom tracking, data collection
- **CRM & Marketing Tools**: Customer management, marketing automation platforms

## Standardized Input Interface

```yaml
task_id: "integration_2025_001"
task_type: "setup_api" | "configure_database" | "integrate_service"
specifications:
  # For API Setup
  api_requirements:
    type: "rest" | "graphql" | "webhook"
    endpoints:
      - path: "/api/contact"
        method: "POST"
        authentication: "api_key"
      - path: "/api/newsletter"
        method: "POST"
        authentication: "none"
    rate_limiting: "100_requests_per_minute"
    
  # For Database Configuration
  database_config:
    type: "postgresql" | "mysql" | "mongodb"
    environment: "production" | "staging" | "development"
    schema_requirements:
      tables: ["users", "orders", "products"]
      relationships: ["users_to_orders", "orders_to_products"]
    
  # For Service Integration
  service_integration:
    service_type: "payment" | "email" | "analytics" | "crm"
    provider: "stripe" | "mailchimp" | "google_analytics"
    integration_points: ["checkout", "form_submission", "user_registration"]

dependencies: ["code_2025_001"] # Often depends on frontend code
output_format: "integration"
priority: "high" | "normal" | "low"
```

## Task Type Handlers

### setup_api
**Purpose**: Create and configure API endpoints and services
**Input Requirements**: api_requirements, authentication, rate_limiting
**Output**: Functioning API with documentation and monitoring
**Subroutines**:
- `design_api_architecture()`
- `implement_endpoint_logic()`
- `setup_authentication_middleware()`
- `create_api_documentation()`

### configure_database
**Purpose**: Set up and configure database systems
**Input Requirements**: database_config, schema_requirements, environment
**Output**: Configured database with optimized schema and connections
**Subroutines**:
- `provision_database_instance()`
- `create_schema_and_tables()`
- `setup_user_permissions()`
- `configure_backup_procedures()`

### integrate_service
**Purpose**: Connect third-party services and external systems
**Input Requirements**: service_integration, provider, integration_points
**Output**: Working integration with error handling and monitoring
**Subroutines**:
- `authenticate_with_service_api()`
- `implement_integration_logic()`
- `setup_error_handling_and_retries()`
- `configure_monitoring_and_alerts()`

## Output Formats

### File Structure
```
/output/integration/
├── apis/
│   ├── contact-api/
│   │   ├── endpoints.js
│   │   ├── middleware.js
│   │   └── documentation.md
│   └── newsletter-api/
├── databases/
│   ├── schema.sql
│   ├── migrations/
│   └── connection-config.js
├── services/
│   ├── stripe-integration.js
│   ├── mailchimp-setup.js
│   └── analytics-tracking.js
└── documentation/
    ├── api-reference.md
    ├── database-schema.md
    └── integration-guide.md
```

### Response Format
```yaml
status: "completed"
task_id: "integration_2025_001"
output:
  format: "integration"
  location: "/output/integration/task_integration_2025_001/"
  endpoints:
    - "https://api.example.com/contact"
    - "https://api.example.com/newsletter"
  database:
    host: "db.example.com"
    name: "production_db"
    status: "connected"
  integrations:
    - service: "stripe"
      status: "active"
      webhook_url: "https://api.example.com/webhooks/stripe"
    - service: "mailchimp"
      status: "active"
      list_id: "abc123def456"
  metadata:
    api_version: "v1"
    database_version: "postgresql_14"
    security_level: "production_ready"
    monitoring_enabled: true
```

## Quality Standards

### API Development
- **RESTful Design**: Proper HTTP methods, status codes, resource naming
- **Security**: Authentication, authorization, input validation, rate limiting
- **Documentation**: Comprehensive API documentation with examples
- **Performance**: Response time optimization, caching, efficient queries

### Database Management
- **Schema Design**: Normalized structure, proper indexing, foreign key constraints
- **Security**: Encrypted connections, user permissions, SQL injection prevention
- **Performance**: Query optimization, connection pooling, monitoring
- **Reliability**: Automated backups, disaster recovery, data integrity

### Integration Quality
- **Error Handling**: Graceful failure handling, retry mechanisms, logging
- **Security**: Secure credential management, API key protection
- **Monitoring**: Health checks, performance metrics, alert systems
- **Documentation**: Clear integration guides, troubleshooting procedures

## Error Handling

### API Errors
- Endpoint configuration failures
- Authentication setup issues
- Rate limiting implementation problems
- Documentation generation errors

### Database Errors
- Connection establishment failures
- Schema migration issues
- Performance optimization problems
- Backup and recovery failures

### Integration Errors
- Third-party service authentication failures
- Webhook delivery problems
- Data synchronization issues
- Service unavailability handling

## Integration Points

### With Other Production Agents
- **code-producer**: Provides frontend code that consumes APIs
- **deployment-producer**: Coordinates database and API deployment
- **data-producer**: Supplies analytics and research data requirements

### With Consultant Agents
- **technical-infrastructure-specialist**: Backend architecture and scaling guidance
- **data-integration-specialist**: Data flow and ETL process design
- **security-specialist**: Security best practices and compliance requirements

## Use When

### Direct Tasks
- Set up REST APIs for frontend applications
- Configure databases for data storage and retrieval
- Integrate payment processing, email services, or analytics
- Implement authentication and user management systems

### Example Workflows
```yaml
# From technical-infrastructure-specialist consultation
task_type: "setup_api"
specifications:
  api_requirements:
    type: "rest"
    endpoints:
      - path: "/api/auth/login"
        method: "POST"
        authentication: "none"
        validation: ["email", "password"]
      - path: "/api/users/profile"
        method: "GET"
        authentication: "jwt_token"
        response_format: "json"
    security_features: ["rate_limiting", "input_validation", "cors"]
    documentation_format: "openapi_3.0"

# From data-integration-specialist consultation
task_type: "integrate_service"
specifications:
  service_integration:
    service_type: "crm"
    provider: "hubspot"
    integration_points: ["contact_form", "newsletter_signup", "user_registration"]
    data_sync_frequency: "real_time"
    fields_to_sync: ["name", "email", "company", "phone", "source"]
```

## Service Categories & Providers

### Payment Processing
- **Stripe**: Credit cards, subscriptions, marketplace payments
- **PayPal**: Digital payments, Express Checkout, recurring billing
- **Square**: In-person and online payments, inventory management
- **Authorize.Net**: Credit card processing, fraud detection

### Email & Communication
- **Mailchimp**: Email marketing, automation, audience management
- **SendGrid**: Transactional emails, email marketing, analytics
- **Twilio**: SMS, voice calls, video communications
- **Intercom**: Customer messaging, live chat, support

### Analytics & Tracking
- **Google Analytics**: Web analytics, conversion tracking, audience insights
- **Mixpanel**: Event tracking, user behavior analysis, funnel analysis
- **Hotjar**: Heatmaps, user recordings, feedback collection
- **Facebook Pixel**: Social media advertising, conversion tracking

### CRM & Business Tools
- **HubSpot**: CRM, marketing automation, sales pipeline
- **Salesforce**: Enterprise CRM, sales automation, customer service
- **Zapier**: Workflow automation, app integrations, trigger-based actions
- **Airtable**: Database management, project tracking, collaboration

### Authentication & Security
- **Auth0**: User authentication, single sign-on, identity management
- **OAuth Providers**: Google, Facebook, GitHub, LinkedIn login
- **Firebase Auth**: User management, social login, custom claims
- **AWS Cognito**: User pools, identity federation, access control

### Database & Storage
- **PostgreSQL**: Relational database, ACID compliance, complex queries
- **MongoDB**: Document database, flexible schema, horizontal scaling
- **Redis**: In-memory cache, session storage, real-time features
- **AWS S3**: File storage, CDN integration, backup solutions