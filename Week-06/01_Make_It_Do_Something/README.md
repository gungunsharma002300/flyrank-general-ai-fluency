# Make It Do Something — General AI Fluency

## What this project demonstrates
This is a simple portfolio with **exactly one dynamic feature**: a real contact form.

The contact form is connected to Formspree:

`https://formspree.io/f/xppzbrrj`

## Data flow
Visitor → Portfolio contact form → Formspree → Real form submission/inbox

## Plain-words backend explanation
The backend is the part of a web application that works behind the visible page. It can receive, process, store, or forward data.

In this project, the visitor enters a name, email, and message in the frontend form. When the visitor clicks **Send message**, the browser sends the form data to the Formspree endpoint. Formspree handles the submission and makes the real submission available through the configured Formspree account/email workflow.

This means the feature is more than a visual button: a real request leaves the portfolio and reaches an external form-handling service.

## Requirement mapping
- Exactly one dynamic feature: contact form
- Free-tier service: Formspree
- Real end-to-end submission: test by submitting the live form
- Plain-words backend explanation: included above
- Live demo: deploy this folder as a static site

## Testing checklist
1. Deploy the project to Vercel, Netlify, or GitHub Pages.
2. Open the deployed URL.
3. Go to **Contact**.
4. Enter a real test name, email, and message.
5. Submit the form.
6. Verify the submission appears in the connected Formspree account/inbox.
7. Take a screenshot showing the successful submission as evidence.
