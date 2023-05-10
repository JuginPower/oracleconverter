import re

def search_replace(orig_line):
            rules = ["NUMBER\(\d+,0\)", "DROP\s+TABLE\s", "\s*ENABLE\s*", 
                     "VARCHAR2", "USING INDEX"]
            solutions = ["INT", "DROP TABLE IF EXISTS ", "", "VARCHAR", ""]

            for rule, solution in zip(rules, solutions):
                orig_line = re.sub(rule, solution, orig_line)
            
            return orig_line
