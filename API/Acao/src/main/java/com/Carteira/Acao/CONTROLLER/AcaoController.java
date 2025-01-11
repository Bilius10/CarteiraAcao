package com.Carteira.Acao.CONTROLLER;

import com.Carteira.Acao.DTO.Recebimento.AcaoDTO;
import com.Carteira.Acao.ENTITY.Acoes;
import com.Carteira.Acao.SERVICES.AcaoService;
import jakarta.validation.Valid;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/acao")
public class AcaoController {

    @Autowired
    private AcaoService acaoService;

    @PostMapping("/save")
    private ResponseEntity<Acoes> saveAcao(@RequestBody @Valid AcaoDTO acaoDTO){

        Acoes acoes = new Acoes();

        BeanUtils.copyProperties(acaoDTO, acoes);
        return ResponseEntity.status(HttpStatus.OK).body(acaoService.saveAcao(acoes));
    }
}