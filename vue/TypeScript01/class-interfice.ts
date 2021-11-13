interface Radio {
    swichRadio(trigger: boolean): void;
}

interface Battery {
    checkBatteryStatus(): void
}

interface RadioWithBattery extends Radio {
    checkBatteryStatus(): void
}

class Car implements Radio {
    swichRadio(trigger: boolean){

    }
}

class Cellphone implements RadioWithBattery {
    swichRadio(trigger: boolean){

    }
    checkBatteryStatus() {

    }
}

