package com.boxinbox.baradho;

import javafx.application.Application;

import com.boxinbox.baradho.Core.Core;
import com.boxinbox.baradho.Core.ICore;
import com.boxinbox.baradho.jfx.vue.IVue;
import com.boxinbox.baradho.jfx.vue.Vue;

import javafx.stage.Stage;
import javafx.animation.AnimationTimer;

public class Baradho {

    private static IVue vue;
    private static Application app = null;
    private static ICore core;

    public Baradho(Stage stage, Application app, TaskBeginner task) {
        if (this.app != null) {
            throw new IllegalStateException("Application already started");
        }
        this.app = app;
        stage.setTitle("Baradho");
        vue = new Vue();
        stage.setScene(vue.getScene());
        stage.show();

        AnimationTimer timer = new AnimationTimer() {
            @Override
            public void handle(long now) {
                vue.dessiner();
            }
        };
        timer.start();
        core = new Core(task);
        task.run(this);
        core.startLoop();

    }

    public static IVue getVue() {
        return vue;
    }

    public static double getLargeur() {
        return Double.parseDouble(app.getParameters().getNamed().getOrDefault("largeur", "800"));
    }

    public static double getHauteur() {
        return Double.parseDouble(app.getParameters().getNamed().getOrDefault("hauteur", "600"));
    }
    
}
