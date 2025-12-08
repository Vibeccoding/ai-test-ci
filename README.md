# AI-Powered Test Generation CI Demo

## Scenario
- **Baseline**: Service with 60% test coverage
- **Change**: New function with 3 branches + 2 error paths (untested)
- **AI Solution**: Automated test gap detection and generation

## Workflow

1. **PR Created** → CI runs analyzer
2. **AI Analysis** → Posts comment with gaps + proposed tests  
3. **Developer** → Accepts/edits/rejects tests
4. **Test PR** → Generated tests in separate PR
5. **CI Run** → 1 test fails, reveals bug
6. **Fix & Rerun** → Coverage jumps to 78%

## Run Demo
```bash
python demo.py
```

## Key Files
- `src/user_service.py` - Service with untested function
- `ci_analyzer.py` - AI gap detection
- `test_generator.py` - Test code generation
- `tests/test_user_service.py` - Existing + generated tests