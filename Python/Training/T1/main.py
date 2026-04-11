def estimate_upload_time(file_size_mb, upload_speed_mbps, retry_count):
    file_size = file_size_mb * 8
    number_of_upload = 1 + retry_count
    total_time = (file_size * number_of_upload)/upload_speed_mbps
    return total_time
