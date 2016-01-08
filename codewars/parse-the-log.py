
url = "http://www.codewars.com/kata/558ecd6398ae4ed3350000c2/train/python"

logparser="^(\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2}\,\d{3}) ([ERROR|INFO|DEBUG]) \[([^\s]+)\:(\w+)\:(\w+)\] (.*?)$"


logparser = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2},\d{3})\s+' \
            r'(DEBUG|ERROR|INFO)\s+\[(\w+):(\w+):?(\w+)?\]\s+(.+)$'