import {Component, inject} from '@angular/core';
import {CommonModule} from '@angular/common';
import {SensorService} from '../sensors.service';
import {SensorData} from "../sensordata";

@Component({
  selector: 'app-home',
  imports: [CommonModule],
  template: `
    <section class="results">
      <h2>Latest Sensor Data</h2>
      <table>
        <thead>
        <tr>
          <th>Timestamp</th>
          <th>Temperature</th>
          <th>Humidity</th>
          <th>Vibration</th>
        </tr>
        </thead>
        <tbody>
        <tr *ngFor="let sensor of sensorDataList">
          <td>{{ sensor.timestamp }}</td>
          <td>{{ sensor.temperature }}°C</td>
          <td>{{ sensor.humidity }}%</td>
          <td>{{ sensor.vibration }}</td>
        </tr>
        </tbody>
      </table>
    </section>
  `,
  styleUrls: ['./home.component.css'],
})

export class HomeComponent {
  sensorDataList: SensorData[] = [];
  sensorService: SensorService = inject(SensorService);

  constructor() {
    this.sensorService.getAllSensorData().then((sensorDataList: SensorData[]) => {
      this.sensorDataList = sensorDataList;
    });
  }
}





