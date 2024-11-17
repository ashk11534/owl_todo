/** @odoo-module **/

import {registry} from '@web/core/registry';
import { Component, useState } from "@odoo/owl";

export class OwlTodoList extends Component{

    setup(){
        this.state = useState({value: 0})
    }

    counterIncrement(){
        this.state.value = this.state.value + 1
    }

    counterDecrement(){
        this.state.value = this.state.value > 0 ? this.state.value - 1 : this.state.value
    }

}

OwlTodoList.template = 'owl_todo.TodoList'

registry.category('actions').add('action_owl_todo', OwlTodoList);