import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TareasService {
  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  // Obtener el token desde localStorage
  private getAuthHeaders(): HttpHeaders {
    const token = localStorage.getItem('token'); // esto es pata recuperar token
    return new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });
  }

  crearUsuario(usuario: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/usuarios`, usuario);
  }

  iniciarSesion(credenciales: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/usuarios/iniciar-sesion`, credenciales);
  }

  obtenerTareasUsuario(idUsuario: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/usuarios/${idUsuario}/tareas`, {
      headers: this.getAuthHeaders()
    });
  }

  crearTarea(tarea: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/tareas`, tarea, {
      //headers: this.getAuthHeaders()
    });
  }

  actualizarTarea(id: string, tarea: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/tareas/${id}`, tarea, {
     // headers: this.getAuthHeaders()
    });
  }

  eliminarTarea(id: string): Observable<any> {
    return this.http.delete(`${this.apiUrl}/tareas/${id}`, {
      //headers: this.getAuthHeaders()
    });
  }

  obtenerTarea(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/tareas/${id}`, {
      //headers: this.getAuthHeaders()
    });
  }

  obtenerUsuario(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/usuarios/${id}`, {
    });
  }
}
