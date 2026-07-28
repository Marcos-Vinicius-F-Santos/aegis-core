import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ChatRequest, ChatResponse } from '../models/chat.model';

@Injectable({
  providedIn: 'root'
})
export class AegisApiService {
  private readonly apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  sendMessage(message: string): Observable<ChatResponse> {
    const payload: ChatRequest = { message };
    return this.http.post<ChatResponse>(`${this.apiUrl}/chat`, payload);
  }
}
