# FlyRank Week 6 — Open It on Your Phone
## Fix Log

**Portfolio:** Gungun Sharma Personal Website
**Track:** General AI Fluency
**Assignment:** Week 6 — Open It on Your Phone

### Fixes made

| Area | Problem found | Fix made | Result |
|---|---|---|---|
| Mobile navigation | Desktop navigation was hidden on small screens with no replacement menu. | Added an accessible hamburger menu with open/close state. | Navigation remains usable on mobile. |
| Mobile buttons | Buttons could become difficult to tap when the viewport is very narrow. | Added a minimum touch-friendly button height and full-width buttons at very small widths. | CTAs are easier to tap. |
| Horizontal overflow | Narrow layouts can create accidental horizontal scrolling. | Added `overflow-x:hidden` and responsive sizing rules. | No intentional horizontal overflow. |
| Responsive project cards | Two-column project layout could become cramped on small screens. | Collapsed project and skill grids to one column below 800px. | Cards stack cleanly on mobile. |
| Typography | Large desktop typography could feel oversized on a phone. | Added mobile-specific `clamp()` sizing and tighter spacing. | Text scales down while remaining readable. |
| Accessibility | Keyboard focus and skip navigation were not explicitly handled. | Added skip link, visible focus styles, semantic labels, and `aria-expanded` menu state. | Better keyboard and assistive-technology usability. |
| Motion | Hover animation had no reduced-motion fallback. | Added `prefers-reduced-motion` handling. | Users who reduce motion are not forced to see hover transitions. |
| External links | External links did not consistently declare `noopener noreferrer`. | Updated external links. | Safer external navigation. |
| Content accuracy | Planned Netflix work was presented too much like a finished case study. | Moved it to a clearly labelled planned/next-work section. | Portfolio does not present unfinished work as completed. |
| Project proof | Project cards had no clear proof link. | Added repository links for the repositories known to be public. | Reviewers can open available proof directly. |

### What was intentionally NOT fabricated

- No fake live URL was inserted.
- No fake phone screenshot was labelled as a real-phone test.
- No fake GitHub repository was created for BugHunter AI.
- No unfinished Netflix project was presented as completed.

### Final manual check still required

The assignment specifically asks for a **real phone** check. Before submission, open the deployed URL on a physical phone and verify the items in `REAL_PHONE_TEST.md`. Add the real before/after phone screenshots to the `evidence/` folder if available.
