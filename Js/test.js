KromBlast.setEvent('launchStart', () => {
    KromBlast.KromId = "KromBlastTest";
});

KromBlast.setEvent('launchFinish', async () => {
    console.log(KromBlast.KromId);
    console.log(await KromBlast.sendCmd("dir"));
});