import {Injectable} from '@angular/core';
import {SensorData} from './sensordata';

@Injectable({
  providedIn: 'root',
})

export class SensorService {
  readonly url = 'http://localhost:5000/api/sensors';

  async getAllSensorData(): Promise<SensorData[]> {
    const data = await fetch(this.url);
    return (await data.json()) ?? [];
  }
}