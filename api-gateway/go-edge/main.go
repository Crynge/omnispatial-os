package main

import (
	"encoding/json"
	"net/http"
)

type Health struct {
	Service string `json:"service"`
	Status  string `json:"status"`
}

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, _ *http.Request) {
		_ = json.NewEncoder(w).Encode(Health{Service: "omnispatial-go-edge", Status: "ok"})
	})
	_ = http.ListenAndServe(":8099", nil)
}

