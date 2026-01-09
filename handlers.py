import random
import re

VALID_EXPR = re.compile(r'(?i)\b([1-9]\d{0,3})?d([1-9]\d{0,3})\b')

def _roll(expr):
    dices = []
    
    def roll_dice(match):
        token = match.group(0)          # ex: "2d6", "1d8", "d20"
        qty = int(match.group(1) or 1)
        faces = int(match.group(2))
        values = [random.randint(1, faces) for _ in range(qty)]
        
        # normalize token (ex: "d20" -> "1d20")
        normalized_token = f"{qty}d{faces}"
        dices.append((match.start(), match.end(), normalized_token, values))
        
        return str(sum(values))
    
    # format and calculate expression
    expr_calculo = re.sub(r'(\d*)d(\d+)', roll_dice, expr)
    result = eval(expr_calculo)
    
    if '.' in str(result) and result % 1 == 0: # remove trailing .0
        result = f"{result}".rstrip('0').rstrip('.') 
    elif isinstance(result, float): # limit 2 decimals
        result = f"{result:.2f}"
    
    # format input with rolled values
    formatted_expr = ""
    last_end = 0
    
    for start, end, token, values in dices:
        between = expr[last_end:start]
        formatted_expr += between
        
        roll_str = f"[{', '.join(map(str, values))}] {token}"
        formatted_expr += roll_str
        
        last_end = end
    
    formatted_expr += expr[last_end:]

    formatted_expr = re.sub(r'([+\-*/])', r' \1 ', formatted_expr)

    formatted_expr = re.sub(r'\s+', ' ', formatted_expr).strip()
    
    return f"` {result} ` ⟵ {formatted_expr}"

def is_valid_expression(expr):
    return bool(VALID_EXPR.search(expr))

def roll(expr):
    try:
        return _roll(expr)
    except Exception:
        return None