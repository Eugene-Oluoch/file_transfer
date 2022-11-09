from user import getting_data_from_user
from directory import print_allowed_directories
from transfer import handle_file_transfer


print_allowed_directories()
user_data = getting_data_from_user()
handle_file_transfer(user_data)


