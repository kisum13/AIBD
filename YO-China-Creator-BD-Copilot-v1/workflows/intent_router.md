# Intent Router

## Step 1: Detect Language
Spanish / Portuguese / Korean / Japanese: reply in same language. English: reply in English.

## Step 2: Detect Intent
Map message to:
project_intro, pricing_negotiation, fixed_fee_question, revenue_share_question, hybrid_model, net_revenue, payment_schedule, deliverables, image_rights, exclusivity, contract_term, sample_projects, content_process, follow_up, signing.

## Step 3: Select Agent
- pricing → agents/pricing_agent.md
- contract → agents/contract_agent.md
- content → agents/content_agent.md
- follow-up → agents/followup_agent.md
- signing → agents/signing_agent.md
- WhatsApp → agents/whatsapp_agent.md
- email → agents/email_agent.md

## Step 4: Generate
Default output:
1. Target-language reply.
2. Chinese translation.
3. Optional note: which module should be updated.

## Step 5: Quality Check
- Does it answer the exact question?
- Does it avoid unsupported promises?
- Does it match the creator’s stage?
- Does it push the next step?
