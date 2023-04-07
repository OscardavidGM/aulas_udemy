from pathlib import Path

LOG_DIR = Path(__file__).parent / 'log.txt'


class log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'error: {msg}')

    def log_sucess(self, msg):
        return self._log(f'sucess: {msg}')


class logFileMixin(log):
    def _log(self, msg):
        msg_fomatada = f'{msg} {self.__class__.__name__}'

        with open(LOG_DIR, 'a', encoding='utf-8') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


class logPrintMixin(log):
    def _log(self, msg):
        print(f'{msg} {self.__class__.__name__}')


if __name__ == '__main__':
    lp = logPrintMixin()
    lp.log_error('Deu ruim')
    lp.log_sucess('Otimo')

    lf = logFileMixin()
    lf.log_error('Deu ruim')
    lf.log_sucess('Otimo')
