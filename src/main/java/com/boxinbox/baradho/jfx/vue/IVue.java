package com.boxinbox.baradho.jfx.vue;

import java.util.Collection;

import com.boxinbox.baradho.jfx.IElement;

import javafx.scene.Scene;

public interface IVue extends Collection<IElement> {
    public boolean dessiner();
    public Scene getScene();
}
