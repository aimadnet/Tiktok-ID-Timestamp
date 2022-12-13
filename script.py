from datetime import datetime

def get_tt_id_timestamp(tt_id: int) -> int:
  return int("{0:08b}".format(tt_id)[:31], 2)

# id of a video of katyperry 
# https://www.tiktok.com/@katyperry/video/7127889434929794347

ts = get_tt_id_timestamp(7127889434929794347)
print(ts)

dt_object = datetime.fromtimestamp(ts)
print("dt_object=", dt_object)
