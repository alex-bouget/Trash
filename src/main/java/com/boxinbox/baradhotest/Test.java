package com.boxinbox.baradhotest;

import com.boxinbox.baradho.Baradho;

public class Test implements com.boxinbox.baradho.TaskBeginner {
    public void run(Baradho baradho) {
        baradho.getVue().add(new MenuPrincipale());
    }
}
