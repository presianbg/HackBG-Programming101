from bank_controller import BankController
from bank_view import BankView
from settings import DATABASE, BLOCK_AFTER_N_ATTEMPTS, BLOCK_FOR_N_MINUTES

controller = BankController(DATABASE,
                            block_afer_n_logins=BLOCK_AFTER_N_ATTEMPTS,
                            block_for_n_minutes=BLOCK_FOR_N_MINUTES)

view = BankView(controller)
view.main_menu()
