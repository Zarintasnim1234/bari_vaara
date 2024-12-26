# utils.py
class Utils:
    @staticmethod
    def validate_nid(nid):
        return len(nid) == 13 and nid.isdigit()
    
    @staticmethod
    def format_currency(amount):
        return f"${amount:,.2f}"
