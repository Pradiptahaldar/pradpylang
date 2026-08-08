PARSER
│
├── Infrastructure
│   ├── parse()                 ✅
│   ├── parse_statement()      ✅
│   ├── parse_block()          ✅
│   ├── advance()              ✅
│   └── expect()               ✅
│
├── Statements
│   ├── keep                   ✅
│   ├── show                   ✅
│   ├── when                   ✅
│   ├── orwhen                 ✅
│   ├── otherwise              ✅
│   ├── repeat                 ✅
│   └── each                   ✅
│
├── Expressions
│   ├── literals               ✅
│   ├── identifiers            ✅
│   ├── parentheses             ✅
│   ├── arithmetic              ✅
│   ├── comparisons             ✅
│   ├── precedence              ✅
│   ├── unary                   ✅
│   ├── booleans                ✅
│   ├── logical operators       ✅
│   └── function calls          ⬜
│
└── Quality
    ├── error handling          ⬜
    └── edge-case testing       ⬜