package com.boxinbox.baradhotest;

import java.util.ArrayList;

import com.boxinbox.baradho.Baradho;
import com.boxinbox.baradho.Core.ICore;
import com.boxinbox.baradho.menu.IMenu;

public class Test implements com.boxinbox.baradho.TaskBeginner {
    ArrayList<IMenu> menus = new ArrayList<IMenu>();

    public void run(Baradho baradho) {
        menus.add(new MenuPrincipale());
        Baradho.getVue().add(menus.get(0));
    }

    @Override
    public void loop(ICore core) {
        if (menus.size() != 0) {
            menus.get(0).menuLoop(core);
            menus.remove(0);
            return;
        }
    }
}
