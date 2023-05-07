import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)

logger.debug("Hello")
logger.getChild('Whatever').setLevel(logging.INFO)

# l2=logger.getChild("first_child")
# l2.info("children are good")
# l3=logger.getChild("2nd child")
# l4=l3.getChild("Grandchild")
# l4.debug("l4")
# l3.debug("l3")


class Whatever:
    def __init__(self):
        pass
    def do_something(self,arg):
        l=logger.getChild("Whatever.do_something")
        l.debug(f"arg: {arg}")
        l.info("doing something")
        return
    
    
Whatever().do_something(123)