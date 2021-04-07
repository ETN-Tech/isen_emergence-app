import React, { Component } from "react";
import {Draggable} from "react-beautiful-dnd"

class Task extends Component        // Correspond à chaque tâche individuelle du Drag and Drop
{
      render() {
        return (
          <Draggable draggableId={this.props.task.id} index={this.props.index}>
            {(provided,snapshot) => (
              <div className="container card text-center"{...provided.draggableProps} {...provided.dragHandleProps} ref={provided.innerRef} isDragging={snapshot.isDragging}>
                {this.props.task.content}
              </div>
            )}
          </Draggable>
        );
      }
    }
export default Task
