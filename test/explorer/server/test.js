

var explorer = new class {
    constructor() {
        KromBlast.krom_id = "Explorer56";
        this.folder = "";
        KromBlast.set_event("initialized", this.listdir.bind(this));
        console.log("Explorer initialized");
    }

    async listdir() {
        this.folder = await KromBlast.explorer.getcwd();
        var file = await KromBlast.explorer.listdir(this.folder);
        var section = document.getElementById("folder");
        section.innerHTML = "";
        file[".."] = true;
        for (const [key, value] of Object.entries(file)) {
            section.appendChild((() => {
                var button = document.createElement("button");
                button.innerHTML = key;
                if (value == true) {
                    button.setAttribute("onclick", "explorer.move(\"" + this.folder + "/" + key + "\")");
                } else {
                    button.disabled = true;
                }
                return button;
            })());
        }

    }

    async move(path) {
        await KromBlast.explorer.move(path);
        await this.listdir();
    }
}();