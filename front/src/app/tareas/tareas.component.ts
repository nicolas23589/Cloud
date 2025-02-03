import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { TareasService } from 'src/services/tareas.service';
@Component({
  selector: 'app-tareas',
  templateUrl: './tareas.component.html',
  styleUrls: ['./tareas.component.css']
})
export class TareasComponent implements OnInit {
  constructor(private location: Location, private tareasService: TareasService){}

  userId: string=''
  user:any;

  tareas:any;

  newTask:any={
      "texto": "",
      "estado":"Pendiente",
      "fecha_tentativa":"",
      "id_usuario": 0,
      "id_categoria":1
  };
  newTaskConfirmation:string='Esperando confirmación para crear tarea...'
  
  ngOnInit(): void {
    
    this.userId = this.location.path().split('/')[2];
    if (this.userId) {
        // Llama al servicio para obtener los datos del restaurante
        this.tareasService.obtenerTareasUsuario(this.userId).subscribe(
          (data) => {
            this.tareas = data;
          },
        );
        this.tareasService.obtenerUsuario(parseInt(this.userId)).subscribe(
          (data) => {
            this.user = data;
          },
        );
      }
    ;
  }

  createTask(){
    this.newTask.id_usuario=this.userId; 
    this.tareasService.crearTarea(this.newTask).subscribe(response => {
      this.newTaskConfirmation = response.mensaje;
    });
  }

  updateTask(tarea:any){
    this.tareasService.actualizarTarea(tarea.id, tarea).subscribe(response => {
    });
    tarea.status="tarea actualizada, refresca para ver cambios"
  }

  deleteTask(tarea:any){
    this.tareasService.eliminarTarea(tarea.id).subscribe(response => {
    });    
    tarea.status="tarea eliminada, refresca para ver cambios"
  }
}




