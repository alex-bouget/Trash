package com.boxinbox.baradho.Core;

import com.boxinbox.baradho.TaskBeginner;

public class Core extends ACore {

    private TaskBeginner task;

    public Core(TaskBeginner task) {
        super();
        this.task = task;
    }

    @Override
    public void loop() {
        while (isRunning) {
            task.loop(this);
            System.out.println("Core loop");
            waitLoop(50);
        }
        System.out.println("Core stopped");
    }
}