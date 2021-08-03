from . import Wallet

class SparrowWallet(Wallet):

    def __init__(self, current_network = "main", qr_density = Wallet.QRMEDIUM, policy = "PKWSH") -> None:
        Wallet.__init__(self, current_network, qr_density, policy)

        self.blink = False

    def set_seed_phrase(self, seed_phrase, passphrase):
        Wallet.set_seed_phrase(self, seed_phrase, passphrase)
        self.ur_decoder = URDecoder()

    def get_name(self) -> str:
        return "Sparrow"

    def set_network(self, network) -> bool:
        if network == "main":
            self.current_network = "main"
            self.hardened_derivation = "m/48h/0h/0h/2h"
        elif network == "test":
            self.current_network = "test"
            self.hardened_derivation = "m/48h/1h/0h/2h"
        else:
            return False

        return True

    def set_qr_density(self, density):
        self.cur_qr_density = density
        if density == Wallet.QRLOW:
            self.qrsize = 50
        elif density == Wallet.QRMEDIUM:
            self.qrsize = 70
        elif density == Wallet.QRHIGH:
            self.qrsize = 120