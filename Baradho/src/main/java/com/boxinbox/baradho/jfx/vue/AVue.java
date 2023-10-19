package com.boxinbox.baradho.jfx.vue;

import javafx.event.EventHandler;
import javafx.event.EventType;

import java.util.concurrent.CopyOnWriteArrayList;

import com.boxinbox.baradho.jfx.BestHandler;
import com.boxinbox.baradho.jfx.Dessin;
import com.boxinbox.baradho.jfx.IElement;

import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.input.KeyEvent;

public abstract class AVue extends CopyOnWriteArrayList<IElement> implements IVue {

    Dessin fond;
    Scene scene;

    public AVue() {
        super();
        fond = new Dessin();
        Group root = new Group();
        scene = new Scene(root);
        root.getChildren().add(fond);
    }

    @Override
    public boolean add(IElement e) {
        if (e instanceof BestHandler) {
            System.out.println("adding event handler");
            scene.addEventHandler(((BestHandler) e).getEventClass(), (EventHandler) e);
        }
        return super.add(e);
    }

    @Override
    public boolean dessiner() {
        boolean dessine = fond.dessiner();
        for (IElement e : this) {
            dessine = e.dessiner(fond.getGc()) && dessine;
        }
        return dessine;
    }

    @Override
    public Scene getScene() {
        return scene;
    }
}
