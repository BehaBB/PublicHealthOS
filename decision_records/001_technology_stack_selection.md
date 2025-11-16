# Architecture Decision Record: Technology Stack Selection
## NIW Evidence: Strategic Technical Decision-Making

## Decision Date
2025-11-01

## Status
Accepted

## Context
Need to select technology stack that balances:
- Rapid prototyping for MVP
- FDA regulatory compliance
- Healthcare security requirements
- Scalability for national deployment

## Decision
Selected Python-based microservices architecture with:
- **Backend**: Python + FastAPI (regulatory documentation advantage)
- **AI/ML**: scikit-learn + pandas (proven healthcare algorithms)
- **Database**: PostgreSQL (HIPAA compliance, audit trails)
- **Infrastructure**: AWS HIPAA-eligible services
- **Integration**: HL7 FHIR for EHR connectivity

## Consequences
### Positive
- Faster FDA approval (Python ecosystem for healthcare)
- Easier hiring (larger talent pool)
- Better regulatory documentation
- Proven healthcare security patterns

### Negative
- Less real-time performance vs Java/Go
- Higher memory usage for some AI workloads
