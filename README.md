# Disneytime

A personal Disney-themed desktop project written in Python, with Tkinter and
bundled artwork.

**Status:** Personal project.

**Maintainer:** [@cptntrps](https://github.com/cptntrps).

## Repository layout

| Path | Purpose |
| --- | --- |
| [Disney8.py](Disney8.py) | Python application entry point |
| Root `*.png` files | Seven bundled artwork assets |
| [.gitignore](.gitignore) | Local environment, Python cache, and OS-file exclusions |
| [.github/SECURITY.md](.github/SECURITY.md) | Private security-reporting instructions |

Keep the artwork beside the application: its existing image references use the
root filenames.

## Setup status

The repository does not yet include a dependency manifest or a documented,
tested Python version. The entry point declares imports for Tkinter, `PIL`, and
`requests`; compatible package versions and installation instructions still need
to be recorded.

## Questions and contributions

Use [issues](https://github.com/cptntrps/Disneytime/issues) for non-sensitive bug
reports, questions, and suggestions. Include your operating system and Python
version when reporting a problem. Keep pull requests focused and describe any
checks you performed.

Do not commit credentials, real environment files, local virtual environments,
or personal data. Use [private reporting](.github/SECURITY.md) for sensitive
security concerns.

## Licensing and artwork

No license is currently declared for the code or artwork. Artwork provenance
and reuse permissions have not yet been documented. Contact the maintainer for
licensing questions.
