# AI Audit — Week 6

## Audit prompts used

1. What could be broken on mobile?
2. What are the accessibility problems?
3. Why could the page feel slow or heavy?

## Audit conclusions applied to the code

### Mobile
- Replace hidden desktop navigation with a usable mobile menu.
- Stack multi-column content on narrow widths.
- Prevent horizontal overflow.
- Keep CTA controls large enough to tap comfortably.
- Scale large headings and spacing down for phone widths.

### Accessibility
- Add a skip-to-content link.
- Provide visible keyboard focus states.
- Use semantic navigation labels.
- Expose the mobile menu state through `aria-expanded` and `aria-controls`.
- Respect `prefers-reduced-motion`.
- Keep link text descriptive.

### Performance
- Keep the site static with no framework or runtime dependency.
- Avoid adding large image assets when none are needed for the current portfolio.
- Keep JavaScript limited to the mobile navigation interaction.
- Keep CSS and HTML local so the page can load without a third-party UI framework.

## Result

The Week 6 revision focuses on responsive behavior, readability, accessibility and truthful project presentation rather than adding unnecessary features.
