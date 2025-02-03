import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TareasService {
  private apiUrl = 'http://localhost:5000'; // URL de la API Flask

  constructor(private http: HttpClient) {}

  // Crear usuario
  crearUsuario(usuario: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/usuarios`, usuario);
  }

  // Iniciar sesión
  iniciarSesion(credenciales: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/usuarios/iniciar-sesion`, credenciales);
  }

  // Obtener tareas de un usuario
  obtenerTareasUsuario(idUsuario: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/usuarios/${idUsuario}/tareas`);
  }

  // Crear tarea
  crearTarea(tarea: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/tareas`, tarea);
  }

  // Actualizar tarea
  actualizarTarea(id: number, tarea: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/tareas/${id}`, tarea);
  }

  // Eliminar tarea
  eliminarTarea(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/tareas/${id}`);
  }

  // Obtener una tarea por ID
  obtenerTarea(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/tareas/${id}`);
  }
}
