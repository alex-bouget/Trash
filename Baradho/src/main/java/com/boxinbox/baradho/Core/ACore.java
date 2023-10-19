package com.boxinbox.baradho.Core;

import javafx.concurrent.Task;

public class ACore implements ICore {

    protected boolean isRunning;
    private Thread thread;

    public ACore() {
        isRunning = false;
    }

    @Override
    public boolean startLoop() {
        if (isRunning) {
            return false;
        }
        isRunning = true;
        Task<Void> task = new Task<Void>() {
            @Override public Void call() {
                loop();
                return null;
            }
        };
        
        Thread thread = new Thread(task);
        thread.setDaemon(true);
        thread.start();
        return true;
    }

    @Override
    public boolean stopLoop() {
        if (!isRunning) {
            return false;
        }
        isRunning = false;
        thread.interrupt();
        return true;
    }

    protected void loop() {
        while (isRunning) {
            waitLoop(50);
        }
    } 

    @Override
    public void waitLoop(int nb) {
        try {
            Thread.sleep(nb);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}