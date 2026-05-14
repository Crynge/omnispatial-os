# Contributing

Thanks for contributing to `omnispatial-os`.

## Expectations

- keep changes testable and production-minded
- update docs whenever public behavior changes
- add or extend tests for engine and API logic
- avoid placeholder-only pull requests for critical platform surfaces

## Local verification

```bash
python -m pytest tests -q
python -m compileall services src tests
npm --prefix frontend-dashboard run build
```

