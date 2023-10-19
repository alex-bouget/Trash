package com.boxinbox.baradho.jfx;


import javafx.event.EventHandler;
import javafx.event.EventType;

public abstract class BestHandler<T extends javafx.event.Event> implements EventHandler<T> {

    EventType<T> eventClass;

    public BestHandler(EventType<T> eventClass) {
        this.eventClass = eventClass;
    }

    public EventType<T> getEventClass() {
        return eventClass;
    }



}