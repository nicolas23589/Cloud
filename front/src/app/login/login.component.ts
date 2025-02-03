import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { TareasService } from 'src/services/tareas.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  nombre: string = '';
  contrasenia: string = '';
  errorMensaje: string = '';

  nombreRegistro: string = '';
  contraseniaRegistro: string = '';
  imgRegistro:string='';
  registroMessage: string = '';

  constructor(private tareasService: TareasService, private router: Router) {}

  iniciarSesion() {
    this.tareasService.iniciarSesion({ nombre: this.nombre, contrasenia: this.contrasenia }).subscribe(
      (response: any) => {
        localStorage.setItem('token', response.token);
        this.router.navigate(['/tareas/' + String(response.usuario.id)]); 
      },
      (error) => {
        console.error('Error en login:', error);
        alert('Credenciales incorrectas');
      }
    );
  }

  registrarse() {
    this.registroMessage = ''; 
    this.tareasService.crearUsuario({ nombre: this.nombreRegistro, contrasenia: this.contraseniaRegistro, imagen:this.imgRegistro }).subscribe(
      (respuesta) => {
        this.registroMessage= respuesta.mensaje
      }
    );
  }
}