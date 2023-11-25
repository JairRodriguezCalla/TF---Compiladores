grammar ScriptGrammar;

program: statement* EOF;

statement: importStatement
         | classDef
         | functionDef
         | assignment
         | ifStatement
         | switchStatement
         | forLoop
         | showCommand
         | runCommand
         | runList
         | runListSave
         | runListLoad
         | runScript
         | interactiveMode
         | exitStatement
         | endStatement
         ;

importStatement: 'get' IDENTIFIER;

classDef: 'class' IDENTIFIER ':' classBody;

classBody: (IDENTIFIER '=' STRING)*;

functionDef: 'def' IDENTIFIER '(' parameters ')' ':' functionBody;

parameters: (IDENTIFIER (',' IDENTIFIER)*)?;

functionBody: (statement)*;

assignment: IDENTIFIER '=' expression;

ifStatement: 'if' condition 'then' statement;

switchStatement: 'switch' expression 'case' expression statement;

forLoop: 'for' IDENTIFIER 'in' 'range' '(' NUMBER ',' NUMBER ')' ':' statement;

showCommand: 'show' '(' expression ')';

runCommand: 'run_command' '(' STRING ',' IDENTIFIER ')';

runList: 'run_list' '(' IDENTIFIER ',' IDENTIFIER ')';

runListSave: 'run_list_save' '(' IDENTIFIER ')';

runListLoad: 'run_list_load' '(' ')';

runScript: 'run_script' '(' STRING ')';

interactiveMode: 'interactive_mode' '(' IDENTIFIER ')';

exitStatement: 'exit';

endStatement: 'end';

condition: expression;

expression: STRING
          | NUMBER
          | IDENTIFIER
          ;

IMPORT: 'get';
CLASS: 'class'; 
FUNCTION: 'def';

IF: 'if'; 
THEN: 'then'; 

SWITCH: 'switch';

CASE: 'case';

FOR: 'for';
IN: 'in';
RANGE: 'range';

SHOW: 'show';

RUN_COMMAND: 'run_command';
RUN_LIST: 'run_list'; 
RUN_LIST_SAVE: 'run_list_save'; 
RUN_LIST_LOAD: 'run_list_load'; 
RUN_SCRIPT: 'run_script';
INTERACTIVE_MODE: 'interactive_mode';

LEFT_P: '(';
RIGHT_P: ')';

COMMA: ',';
COLON: ':';
EQUALS: '=';

EXIT: 'exit';
END: 'end';

NUMBER : [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';
WS: [ \t\n\r\f]+ -> skip ;
COMMENT: '#' ~[\r\n]* -> skip;