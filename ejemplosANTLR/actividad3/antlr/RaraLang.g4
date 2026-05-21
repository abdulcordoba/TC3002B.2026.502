grammar RaraLang;

prog : INT* EOF ;

expr
    : INT           #int
    ;

// ─── Literales ────────────────────────────────────────────────────────────────

INT         : [0-9]+ ;

// ─── Infraestructura ──────────────────────────────────────────────────────────

NEWLINE : [\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
WS      : [ \t]+  -> skip ;
