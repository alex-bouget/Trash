const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

var KromBlast = new class {
    constructor() {
        this.KromId = 'null';
        this.isInKrom = false;
        this.allReturn = {};
        this.KromData = [];
        this.event = {
            launchStart: this.eventNull,
            launchFinish: this.eventNull,
        };
    }

    endLaunch() {
        this.isInKrom = true;
        this.event['launchFinish']();
    }

    eventNull() {}

    setEvent(key, func) {
        if (key in this.event) {
            this.event[key] = func;
        }
    }

    launch() {
        this.event['launchStart']();
        return true;
    }

    async sendCmd(cmd) {
        this.allReturn[cmd] = [];
        this.KromData.push([this.KromId, cmd]);
        do {
            await delay(100);
        } while (!this.allReturn[cmd].includes("*end"));
        var data = this.allReturn[cmd];
        delete this.allReturn[cmd];
        return data;
    }

    getLastCmd() {
        if (this.KromData.length == 0) {
            return "null";
        }
        var data = this.KromData[0];
        this.KromData.splice(0, 1);
        return data[0]+"*:!:*"+data[1];
    }
    

    returnCmd(cmd, data) {
        this.allReturn[cmd].push(data);
    }
}