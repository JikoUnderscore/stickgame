class CD:
    '''
    Minimalnata prodylzitelnost ot vreme, kojato igracyt trjabva da izcaka sled kato izpolzva umenie/sposobnost ili predmet,
    predi da moze da se izpolzva otnovo.

    Tova seldi vremeto na vseki klas, kojto go nasledi.
    '''
    def __init__(self):
        self.ljavaAtakaCD = 0
        self.djasnaAtakaCD = 0
        self.ljavaAtaka = 0
        self.djasnaAtaka = 0
        self.GCD = 0
        self.GCDmax = 1
        self.ljavaAtakaMAX = 0
        self.djasnaAtakaMAX = 0

        self.raznoCD = 0
        self.raznoCDMAX = 0

        self.zastita = 0
        self.HP = 100
        self.HPnstojast = self.HP
        self.attackPower = 0
        self.hitChance = 90
        self.crit = 0
        self.critMultiplier = [0]
        self.dodge = 1

    def cool_down_START(self, COOLDOWN_dt):
        self._ljava_ataka_CD(COOLDOWN_dt)
        self._djasna_ataka_CD(COOLDOWN_dt)
        self._razno_CD(COOLDOWN_dt)

    def _ljava_ataka_CD(self, COOLDOWN_dt):
        if self.ljavaAtakaCD >= self.ljavaAtakaMAX:
            self.ljavaAtakaCD = 0
        elif self.ljavaAtakaCD > 0:
            self.ljavaAtakaCD += COOLDOWN_dt

    def _djasna_ataka_CD(self, COOLDOWN_dt):
        if self.djasnaAtakaCD >= self.djasnaAtakaMAX:
            self.djasnaAtakaCD = 0
        elif self.djasnaAtakaCD > 0:
            self.djasnaAtakaCD += COOLDOWN_dt

    def _razno_CD(self, COOLDOWN_dt):
        if self.raznoCD >= self.raznoCDMAX:
            self.raznoCD = 0
        elif self.raznoCD > 0:
            self.raznoCD += COOLDOWN_dt

    def global_cool_down(self, COOLDOWN_dt):
        if self.GCD >= self.GCDmax:
            self.GCD = 0
        elif self.GCD > 0:
            self.GCD += COOLDOWN_dt

