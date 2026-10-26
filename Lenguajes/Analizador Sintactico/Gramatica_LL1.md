# Gramática LL(1) Formal del Lenguaje Lua (Lua 5.5)

Gramática adaptada para el analizador sintáctico descendente LL(1), ordenada siguiendo estrictamente la especificación oficial de **Complete syntax** de Lua 5.5, con las producciones complementarias ubicadas inmediatamente debajo de su regla principal, no terminales en MAYÚSCULAS y utilizando los nombres de tokens exactos definidos en [`Lexico.py`](file:///c:/Users/Computador/2026-2/Lenguajes/AnalizadorLexico/Lexico.py).

---

## 1. Catálogo de Símbolos Terminales (Tokens de Lexico.py)

- **Palabras reservadas**: `and`, `break`, `do`, `else`, `elseif`, `end`, `false`, `for`, `function`, `global`, `goto`, `if`, `in`, `local`, `nil`, `not`, `or`, `repeat`, `return`, `then`, `true`, `until`, `while`
- **Funciones estándar permitidas como identificadores**: `error`, `pcall`, `print`, `warn`, `xpcall`
- **Identificadores y literales**: `id`, `valor_numerico`, `cadena_de_caracteres`
- **Operadores y símbolos**:
  - Delimitadores: `tkn_semicolon` (`;`), `tkn_colon` (`:`), `tkn_comma` (`,`), `tkn_period` (`.`), `tkn_assign` (`=`)
  - Paréntesis y llaves: `tkn_opening_par` (`(`), `tkn_closing_par` (`)`), `tkn_opening_bra` (`[`), `tkn_closing_bra` (`]`), `tkn_opening_key` (`{`), `tkn_closing_key` (`}`)
  - Aritméticos: `tkn_plus` (`+`), `tkn_minus` (`-`), `tkn_times` (`*`), `tkn_div` (`/`), `tkn_floor_div` (`//`), `tkn_power` (`^`), `tkn_mod` (`%`)
  - Relacionales: `tkn_equal` (`==`), `tkn_neq` (`~=`), `tkn_less` (`<`), `tkn_leq` (`<=`), `tkn_greater` (`>`), `tkn_geq` (`>=`)
  - Bitwise: `tkn_bit_and` (`&`), `tkn_bit_or` (`|`), `tkn_bitex_or` (`~`), `tkn_left_shift` (`<<`), `tkn_right_shift` (`>>`)
  - Especiales: `tkn_concat` (`..`), `tkn_varargs` (`...`), `tkn_goto` (`::`), `tkn_length` (`#`)
- **Elemento no léxico (fin de archivo)**: `final_de_archivo`
- **Cadena vacía**: `epsilon`

---

## 2. Producciones de la Gramática LL(1)

### 2.1 CHUNK
```ebnf
CHUNK -> BLOCK final_de_archivo
```

### 2.2 BLOCK
```ebnf
BLOCK -> STAT_LIST RETSTAT_OPCIONAL

STAT_LIST -> STAT STAT_LIST
           | epsilon
```

### 2.3 STAT
```ebnf
STAT -> tkn_semicolon
      | do BLOCK end
      | while EXP do BLOCK end
      | repeat BLOCK until EXP
      | if EXP then BLOCK IF_TAIL
      | for NAME FOR_TAIL
      | function FUNCNAME FUNCBODY
      | local LOCAL_TAIL
      | global GLOBAL_TAIL
      | break
      | goto NAME
      | LABEL
      | NAME STAT_IDENT_TAIL

IF_TAIL -> elseif EXP then BLOCK IF_TAIL
         | else BLOCK end
         | end

FOR_TAIL -> tkn_assign EXP tkn_comma EXP FOR_STEP_OPCIONAL do BLOCK end
          | NAMELIST_TAIL in EXPLIST do BLOCK end

FOR_STEP_OPCIONAL -> tkn_comma EXP
                   | epsilon

LOCAL_TAIL -> function NAME FUNCBODY
            | NAME ATTNAMELIST_TAIL LOCAL_ASIGNACION_OPCIONAL

GLOBAL_TAIL -> function NAME FUNCBODY
             | NAME ATTNAMELIST_TAIL GLOBAL_ASIGNACION_OPCIONAL

LOCAL_ASIGNACION_OPCIONAL -> tkn_assign ASIGN_EXPLIST
                           | epsilon

GLOBAL_ASIGNACION_OPCIONAL -> tkn_assign ASIGN_EXPLIST
                            | epsilon

STAT_IDENT_TAIL -> tkn_period NAME STAT_IDENT_TAIL
                 | tkn_opening_bra EXP tkn_closing_bra STAT_IDENT_TAIL
                 | tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
                 | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
                 | tkn_comma VARLIST_ASSIGN
                 | tkn_assign ASIGN_EXPLIST
```

### 2.4 ATTNAMELIST_TAIL
```ebnf
ATTNAMELIST_TAIL -> ATTRIB_OPCIONAL ATTNAMELIST_TAIL_RESTO

ATTNAMELIST_TAIL_RESTO -> tkn_comma NAME ATTNAMELIST_TAIL
                        | epsilon
```

### 2.5 ATTRIB
```ebnf
ATTRIB -> tkn_less NAME tkn_greater

ATTRIB_OPCIONAL -> ATTRIB
                 | epsilon
```

### 2.6 RETSTAT
```ebnf
RETSTAT -> return EXPLIST_OPCIONAL SEMICOLON_OPCIONAL

RETSTAT_OPCIONAL -> RETSTAT
                  | epsilon

SEMICOLON_OPCIONAL -> tkn_semicolon
                    | epsilon
```

### 2.7 LABEL
```ebnf
LABEL -> tkn_goto NAME tkn_goto
```

### 2.8 FUNCNAME
```ebnf
FUNCNAME -> NAME FUNCNAME_TAIL

FUNCNAME_TAIL -> tkn_period NAME FUNCNAME_TAIL
               | tkn_colon NAME
               | epsilon
```

### 2.9 VARLIST_ASSIGN
```ebnf
VARLIST_ASSIGN -> VAR VARLIST_ASSIGN_TAIL

VARLIST_ASSIGN_TAIL -> tkn_comma VARLIST_ASSIGN
                     | tkn_assign ASIGN_EXPLIST
```

### 2.10 VAR
```ebnf
VAR -> NAME VAR_SUFFIX

VAR_SUFFIX -> tkn_period NAME VAR_SUFFIX
            | tkn_opening_bra EXP tkn_closing_bra VAR_SUFFIX
            | epsilon
```

### 2.11 NAMELIST_TAIL
```ebnf
NAMELIST_TAIL -> tkn_comma NAME NAMELIST_TAIL
               | epsilon
```

### 2.12 ASIGN_EXP y ASIGN_EXPLIST
```ebnf
ASIGN_EXP -> EXP
           | FUNCTIONDEF
           | tkn_varargs

ASIGN_EXPLIST -> ASIGN_EXP ASIGN_EXPLIST_TAIL

ASIGN_EXPLIST_TAIL -> tkn_comma ASIGN_EXP ASIGN_EXPLIST_TAIL
                    | epsilon
```

### 2.13 EXPLIST
```ebnf
EXPLIST -> EXP EXPLIST_TAIL

EXPLIST_TAIL -> tkn_comma EXP EXPLIST_TAIL
              | epsilon

EXPLIST_OPCIONAL -> EXPLIST
                  | epsilon
```

### 2.14 EXP
```ebnf
EXP -> UNOP EXP
     | TERM EXP_TAIL

EXP_TAIL -> BINOP EXP
          | epsilon

TERM -> nil
      | false
      | true
      | valor_numerico
      | cadena_de_caracteres
      | TABLECONSTRUCTOR
      | PREFIXEXP
```

### 2.14 PREFIXEXP
```ebnf
PREFIXEXP -> NAME PREFIX_SUFFIX
           | tkn_opening_par EXP tkn_closing_par PREFIX_SUFFIX

PREFIX_SUFFIX -> tkn_period NAME PREFIX_SUFFIX
               | tkn_opening_bra EXP tkn_closing_bra PREFIX_SUFFIX
               | tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par PREFIX_SUFFIX
               | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par PREFIX_SUFFIX
               | epsilon
```

### 2.15 CALL_TAIL
```ebnf
CALL_TAIL -> tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
           | tkn_colon NAME tkn_opening_par EXPLIST_OPCIONAL tkn_closing_par CALL_TAIL
           | tkn_period NAME STAT_IDENT_TAIL
           | tkn_opening_bra EXP tkn_closing_bra STAT_IDENT_TAIL
           | epsilon
```

### 2.16 FUNCTIONDEF
```ebnf
FUNCTIONDEF -> function FUNCBODY
```

### 2.17 FUNCBODY
```ebnf
FUNCBODY -> tkn_opening_par PARLIST_OPCIONAL tkn_closing_par BLOCK_FUNC end

BLOCK_FUNC -> STAT_LIST RETSTAT_OPCIONAL

PARLIST_OPCIONAL -> PARLIST
                  | epsilon
```

### 2.18 PARLIST
```ebnf
PARLIST -> VARARGPARAM
         | NAME PARLIST_TAIL

PARLIST_TAIL -> tkn_comma PARLIST_RESTO
              | epsilon

PARLIST_RESTO -> VARARGPARAM
               | NAME PARLIST_TAIL
```

### 2.19 VARARGPARAM
```ebnf
VARARGPARAM -> tkn_varargs VARARG_NAME_OPCIONAL

VARARG_NAME_OPCIONAL -> NAME
                      | epsilon
```

### 2.20 TABLECONSTRUCTOR
```ebnf
TABLECONSTRUCTOR -> tkn_opening_key FIELDLIST_OPCIONAL tkn_closing_key
```

### 2.21 FIELDLIST
```ebnf
FIELDLIST -> FIELD FIELDLIST_TAIL

FIELDLIST_OPCIONAL -> FIELDLIST
                    | epsilon

FIELDLIST_TAIL -> FIELDSEP FIELDLIST_RESTO
                | epsilon

FIELDLIST_RESTO -> FIELD FIELDLIST_TAIL
                 | epsilon
```

### 2.22 FIELD
```ebnf
FIELD -> tkn_opening_bra EXP tkn_closing_bra tkn_assign ASIGN_EXP
       | NAME FIELD_IDENT_TAIL
       | UNOP EXP
       | nil EXP_TAIL
       | false EXP_TAIL
       | true EXP_TAIL
       | valor_numerico EXP_TAIL
       | cadena_de_caracteres EXP_TAIL
       | tkn_varargs EXP_TAIL
       | FUNCTIONDEF EXP_TAIL
       | TABLECONSTRUCTOR EXP_TAIL
       | tkn_opening_par EXP tkn_closing_par PREFIX_SUFFIX EXP_TAIL

FIELD_IDENT_TAIL -> tkn_assign ASIGN_EXP
                  | PREFIX_SUFFIX EXP_TAIL
```

### 2.23 FIELDSEP
```ebnf
FIELDSEP -> tkn_comma
          | tkn_semicolon
```

### 2.24 BINOP
```ebnf
BINOP -> tkn_plus
       | tkn_minus
       | tkn_times
       | tkn_div
       | tkn_floor_div
       | tkn_power
       | tkn_mod
       | tkn_bit_and
       | tkn_bitex_or
       | tkn_bit_or
       | tkn_right_shift
       | tkn_left_shift
       | tkn_concat
       | tkn_less
       | tkn_leq
       | tkn_greater
       | tkn_geq
       | tkn_equal
       | tkn_neq
       | and
       | or
```

### 2.25 UNOP
```ebnf
UNOP -> tkn_minus
      | not
      | tkn_length
```

### 2.26 NAME
```ebnf
NAME -> id
      | error
      | pcall
      | print
      | warn
      | xpcall
```
